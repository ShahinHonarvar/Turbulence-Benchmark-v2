def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[10:76]
    for i in range(len(substring)):
        for j in range(i + 10, min(i + 21, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if potential_palindrome == potential_palindrome[::-1] and 10 <= len(potential_palindrome) <= 20:
                result.add(potential_palindrome)
    return result