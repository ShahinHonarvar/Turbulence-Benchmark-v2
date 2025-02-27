def palindromes_of_specific_lengths(s):
    left, right = (24, 97)
    results = set()
    while left <= right:
        for i in range(left, right + 1):
            for j in range(i, right + 1):
                substring = s[i:j + 1].lower()
                if substring == substring[::-1] and len(substring) >= 10 and (len(substring) <= 36):
                    results.add(substring)
        left += 1
        right -= 1
    return results