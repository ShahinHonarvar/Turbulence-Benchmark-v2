def palindromes_of_specific_lengths(s):
    substring = s[17:66]
    palindromes_set = set()
    for length in range(23, 37):
        for i in range(len(substring) - length + 1):
            sub_palindrome = substring[i:i + length].lower()
            if sub_palindrome == sub_palindrome[::-1] and sub_palindrome.isalpha():
                palindromes_set.add(sub_palindrome)
    return palindromes_set