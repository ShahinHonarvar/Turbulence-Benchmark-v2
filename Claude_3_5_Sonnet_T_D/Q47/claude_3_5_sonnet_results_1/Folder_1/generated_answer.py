def palindromes_of_specific_lengths(input_string):
    result = set()
    substring = input_string[15:90]
    for i in range(len(substring)):
        for j in range(i + 40, min(i + 73, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((char.lower() for char in potential_palindrome if char.isalpha()))
            if 40 <= len(cleaned_palindrome) <= 72 and cleaned_palindrome == cleaned_palindrome[::-1]:
                result.add(cleaned_palindrome)
    return result