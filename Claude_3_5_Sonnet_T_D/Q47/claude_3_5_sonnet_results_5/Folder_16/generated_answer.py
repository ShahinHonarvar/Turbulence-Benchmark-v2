def palindromes_of_specific_lengths(string):
    result = set()
    substring = string[15:87]
    for i in range(len(substring)):
        for j in range(i + 51, min(i + 61, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((char.lower() for char in potential_palindrome if char.isalpha()))
            if cleaned_palindrome == cleaned_palindrome[::-1] and 51 <= len(cleaned_palindrome) <= 60:
                result.add(potential_palindrome)
    return result