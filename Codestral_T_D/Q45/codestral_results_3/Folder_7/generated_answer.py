from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):
    s = s[1:10].lower()
    c = Counter(s)
    chars = [k for k, v in c.items() for _ in range(v // 2)]
    palindromes = set()
    for i in range(7, len(s) + 1):
        for p in permutations(chars, i // 2):
            temp = list(p)
            if i % 2 == 0:
                temp += temp[::-1]
            else:
                mid = [k for k, v in c.items() if v % 2 == 1]
                if mid:
                    temp += mid + temp[::-1]
            palindromes.add(''.join(temp))
    return palindromes