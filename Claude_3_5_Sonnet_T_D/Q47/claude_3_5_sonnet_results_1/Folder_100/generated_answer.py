def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[29:97]
    for i in range(len(substring)):
        for j in range(i + 12, min(i + 19, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((char.lower() for char in potential_palindrome if char.isalpha()))
            if 12 <= len(cleaned_palindrome) <= 18 and cleaned_palindrome == cleaned_palindrome[::-1]:
                result.add(cleaned_palindrome)
    return result