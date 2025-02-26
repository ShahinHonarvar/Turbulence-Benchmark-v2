def palindromes_of_specific_lengths(s):
    substring = s[31:75]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 23, min(i + 40, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join(filter(str.isalpha, potential_palindrome)).lower()
            if 23 <= len(cleaned_palindrome) <= 39 and cleaned_palindrome == cleaned_palindrome[::-1]:
                result.add(cleaned_palindrome)
    return result