def palindromes_of_specific_lengths(s):
    result = set()
    s = ''.join((c for c in s if c.isalpha()))
    substring = s[11:97].lower()
    length_range = range(45, 53)
    n = len(substring)
    for start in range(n):
        for length in length_range:
            end = start + length
            if end > n:
                break
            possible_palindrome = substring[start:end]
            if possible_palindrome == possible_palindrome[::-1]:
                result.add(selected_palindrome)
    return result