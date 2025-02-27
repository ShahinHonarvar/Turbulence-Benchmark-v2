def all_substring_of_size_n(s):

    def generate_substrings(s, start, end):
        if end - start == 120:
            yield s[start:end]
        else:
            for i in range(start, end):
                yield from generate_substrings(s, i + 1, end)
    seen = set()
    result = []
    for substring in generate_substrings(s, 0, len(s)):
        if substring not in seen:
            seen.add(substring)
            result.append(substring)
    return result