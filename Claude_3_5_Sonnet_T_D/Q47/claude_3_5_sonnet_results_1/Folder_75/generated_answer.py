def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[31:75]
    substring = ''.join((char.lower() for char in substring if char.isalpha()))
    for length in range(23, 40):
        for i in range(len(substring) - length + 1):
            potential_palindrome = substring[i:i + length]
            if potential_palindrome == potential_palindrome[::-1]:
                result.add(potential_palindrome)
    return result