def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[18:99]
    for i in range(len(substring)):
        for j in range(i + 31, min(i + 52, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if potential_palindrome == potential_palindrome[::-1] and 31 <= len(potential_palindrome) <= 51:
                result.add(potential_palindrome)
    return result