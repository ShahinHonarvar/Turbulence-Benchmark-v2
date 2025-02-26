def palindromes_of_specific_lengths(s):
    start_index = 18
    end_index = 87
    min_length = 38
    max_length = 60
    result = set()
    substring = s[start_index:end_index + 1].lower()
    for length in range(min_length, max_length + 1):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if all((char.isalpha() for char in candidate)):
                if candidate == candidate[::-1]:
                    result.add(candidate)
    return result