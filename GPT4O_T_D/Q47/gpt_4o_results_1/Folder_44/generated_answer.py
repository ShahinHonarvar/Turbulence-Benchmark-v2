def palindromes_of_specific_lengths(s):
    start, end = (18, 98)
    min_length, max_length = (31, 51)
    substr = s[start:end + 1].lower()
    palindromes = set()
    for i in range(len(substr)):
        for length in range(min_length, max_length + 1):
            if i + length <= len(substr):
                candidate = substr[i:i + length]
                if all((c.isalpha() for c in candidate)):
                    if candidate == candidate[::-1]:
                        palindromes.add(s[start + i:start + i + length])
    return palindromes