def palindromes_of_specific_lengths(s):
    substring = s[45:99]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 40, min(i + 48, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if potential_palindrome == potential_palindrome[::-1] and 40 <= len(potential_palindrome) <= 47:
                result.add(potential_palindrome)
    return result