def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for length in range(len(s), 140, -1):
        for i in range(len(s) - length + 1):
            query = s[i:i + length]
            if query == query[::-1] and query.isalpha():
                result.add(query)
    return result