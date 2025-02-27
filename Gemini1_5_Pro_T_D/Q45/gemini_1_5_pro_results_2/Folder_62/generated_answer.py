from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter([string[i].lower() for i in range(0, 9) if string[i].isalpha()])
    palindromes = set()
    for perm in {''.join(p) for i in range(7, len(letters) + 1) for p in permutations(letters.elements(), i)}:
        if perm == perm[::-1]:
            flag = True
            perm_counter = Counter(perm)
            for c in perm_counter:
                if letters[c] < perm_counter[c]:
                    flag = False
                    break
            if flag:
                palindromes.add(perm)
    return palindromes