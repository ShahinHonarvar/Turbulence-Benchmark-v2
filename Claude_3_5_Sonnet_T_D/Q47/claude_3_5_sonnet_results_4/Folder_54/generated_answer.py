def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[27:78]
    for i in range(len(substring)):
        for j in range(i + 18, min(i + 20, len(substring) + 1)):
            potential_palindrome = ''.join((char.lower() for char in substring[i:j] if char.isalpha()))
            if potential_palindrome == potential_palindrome[::-1] and 18 <= len(potential_palindrome) <= 19:
                result.add(substring[i:j])
    return result