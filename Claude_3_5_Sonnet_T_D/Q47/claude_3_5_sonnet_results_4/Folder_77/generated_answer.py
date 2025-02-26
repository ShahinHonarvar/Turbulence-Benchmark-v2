def palindromes_of_specific_lengths(string):
    substring = string[103:277]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 100, min(i + 170, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((char.lower() for char in potential_palindrome if char.isalpha()))
            if cleaned_palindrome == cleaned_palindrome[::-1] and 100 <= len(cleaned_palindrome) <= 169:
                result.add(cleaned_palindrome)
    return result