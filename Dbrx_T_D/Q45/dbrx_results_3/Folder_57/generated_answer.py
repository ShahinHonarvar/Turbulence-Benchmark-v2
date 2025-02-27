def palindromes_between_indices(s):
    result = set()
    for i in range(2, 6):
        for j in range(i, 6):
            substring = s[2:6][i:j + 1]
            if len(substring) >= 5:
                substring = substring.lower()
                palindrome = substring + substring[::-1]
                if len(palindrome) >= 5 and palindrome in result:
                    continue
                result.add(palindrome)
    return result