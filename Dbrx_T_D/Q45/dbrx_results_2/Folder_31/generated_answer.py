from collections import defaultdict

def palindromes_between_indices(s):
    eng_letters = {chr(i).lower() for i in range(ord('a'), ord('z') + 1)}
    valid_letters = ''.join((c for c in s.lower() if c in eng_letters))
    if len(valid_letters) < 6:
        return set()
    palindromes = set()
    for i in range(1, 9):
        for j in range(i, 9):
            substring = valid_letters[i - 1:j]
            if len(substring) < 6:
                continue
            if len(substring) == 6:
                palindromes.add(substring)
                continue
            substring_set = set(substring)
            if len(substring_set) == 1:
                palindromes.add(substring_set.pop() * len(substring))
            else:
                for k in range(3, len(substring) + 1, 2):
                    if k % 2 == 0 and substring[:k // 2] == substring[-k // 2:][::-1]:
                        palindromes.add(substring[:k // 2] + substring[k // 2:k // 2 + len(substring) // 2] + substring[k // 2:][::-1])
                    elif k % 2 == 1 and substring[:k // 2] == substring[-k // 2 - 1:][::-1]:
                        palindromes.add(substring[:k // 2] + substring[k // 2])
    return palindromes