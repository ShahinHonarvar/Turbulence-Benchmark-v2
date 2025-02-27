def palindromes_of_specific_lengths(s):
    sub = s[44:100]
    result = set()
    length_range = range(13, 43)
    for start in range(len(sub)):
        for length in length_range:
            end = start + length
            if end > len(sub):
                break
            potential_palindrome = sub[start:end]
            filtered = ''.join(filter(str.isalpha, potential_palindrome))
            if len(filtered) == length and filtered.lower() == filtered[::-1].lower():
                result.add(filtered.lower())
    return result