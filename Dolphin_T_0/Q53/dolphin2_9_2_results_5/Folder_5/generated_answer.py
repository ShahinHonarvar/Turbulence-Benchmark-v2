def palindrome_of_length_at_least_n(text: str) -> set:
    text_lowered = text.lower()
    result = set()
    for i in range(len(text_lowered) - 45):
        for length in range(46, len(text_lowered) - i + 1):
            candidate = text_lowered[i:i + length]
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result