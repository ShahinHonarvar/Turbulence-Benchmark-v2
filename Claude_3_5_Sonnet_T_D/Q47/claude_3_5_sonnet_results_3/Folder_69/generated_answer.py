def palindromes_of_specific_lengths(s):
    result = set()
    substr = s[11:97]
    substr = ''.join((char.lower() for char in substr if char.isalpha()))
    for length in range(45, 53):
        for i in range(len(substr) - length + 1):
            segment = substr[i:i + length]
            if segment == segment[::-1]:
                result.add(segment)
    return result