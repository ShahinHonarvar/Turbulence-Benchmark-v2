def palindromes_between_indices(s):
    substring = s[3:9]
    substring_letters = [c for c in substring if c.isalpha()]
    substring_letters = ''.join(substring_letters).lower()
    len_substring_letters = len(substring_letters)
    palindromes_set = set()
    if len_substring_letters < 4:
        return palindromes_set
    for i in range(len_substring_letters - 3):
        for j in range(i + 3, len_substring_letters):
            if substring_letters[i] != substring_letters[j]:
                continue
            else:
                for k in range(i + 1, j):
                    if substring_letters[k] != substring_letters[i]:
                        break
                else:
                    palindromes_set.add(substring_letters)
    return palindromes_set