def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[16:78]
    for i in range(len(substring)):
        for j in range(i + 43, min(i + 48, len(substring) + 1)):
            palindrome = substring[i:j]
            if palindrome.isalpha() and palindrome.lower() == palindrome.lower()[::-1]:
                result.add(palindrome)
    return result