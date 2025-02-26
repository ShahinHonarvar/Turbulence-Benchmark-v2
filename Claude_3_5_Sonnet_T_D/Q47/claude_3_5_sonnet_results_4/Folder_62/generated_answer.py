def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[26:88]
    for i in range(len(substring)):
        for j in range(i + 52, min(i + 57, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if potential_palindrome == potential_palindrome[::-1] and 52 <= len(potential_palindrome) <= 56:
                result.add(potential_palindrome)
    return result