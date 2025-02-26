def palindromes_of_specific_lengths(s):
    substring = s[31:75]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 23, min(i + 40, len(substring) + 1)):
            palindrome = substring[i:j]
            if palindrome.isalpha() and palindrome.lower() == palindrome.lower()[::-1]:
                result.add(palindrome)
    return result