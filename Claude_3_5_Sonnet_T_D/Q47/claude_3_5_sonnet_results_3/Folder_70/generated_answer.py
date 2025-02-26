def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[10:71]
    for i in range(len(substring)):
        for j in range(i + 24, min(i + 53, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((char.lower() for char in potential_palindrome if char.isalpha()))
            if 24 <= len(cleaned_palindrome) <= 52 and cleaned_palindrome == cleaned_palindrome[::-1]:
                result.add(cleaned_palindrome)
    return result