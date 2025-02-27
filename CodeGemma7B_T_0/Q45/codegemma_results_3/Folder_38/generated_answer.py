import re
  from itertools import permutations

def palindromes_between_indices(text):
    text = re.sub('[^a-zA-Z]', '', text)
    text = text.lower()
    if len(text) < 5:
        return set()
    palindromes = set()
    for i in range(3, 9):
        for j in range(i + 1, 9):
            for k in range(j + 1, 9):
                for l in range(k + 1, 9):
                    for m in range(l + 1, 9):
                        for p in permutations(text[i:m + 1]):
                            palindrome = ''.join(p)
                            if len(palindrome) >= 5:
                                palindromes.add(palindrome)
    return palindromes