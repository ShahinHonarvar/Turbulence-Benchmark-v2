def palindromes_between_indices(s):
    palindromes = set()
    length = len(s)
    if length >= 10:
        substring = s[5:10]
        for length in range(3, len(substring) + 1):
            for i in range(0, length):
                for j in range(i + length, length + i + 1):
                    sub = substring[i:j]
                    if sub == sub[::-1]:
                        palindromes.add(sub.lower())
    return palindromes