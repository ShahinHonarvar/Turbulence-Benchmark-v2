def palindromes_of_specific_lengths(s):
    substring = s[105:281]
    lengths = range(136, 152)
    results = set()
    for length in lengths:
        for i in range(0, len(substring) - length + 1):
            chunk = substring[i:i + length].lower()
            if chunk == chunk[::-1] and chunk.isalpha():
                results.add(chunk)
    return results