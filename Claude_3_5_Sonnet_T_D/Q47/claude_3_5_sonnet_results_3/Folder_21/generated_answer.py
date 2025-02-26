def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[100:296]
    for i in range(len(substring)):
        for j in range(i + 136, min(i + 161, len(substring) + 1)):
            palindrome = substring[i:j]
            if palindrome.isalpha() and palindrome.lower() == palindrome.lower()[::-1]:
                result.add(palindrome)
    return result