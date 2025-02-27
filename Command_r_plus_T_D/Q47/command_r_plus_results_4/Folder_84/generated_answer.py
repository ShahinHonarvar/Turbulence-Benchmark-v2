def palindromes_of_specific_lengths(input_string: str) -> set:
    palindromes = set()
    substring = input_string[22:78].lower()
    for length in range(13, 41):
        for i in range(len(substring) - length + 1):
            segment = substring[i:i + length]
            if segment == segment[::-1] and segment.isalpha():
                palindromes.add(segment)
    return palindromes