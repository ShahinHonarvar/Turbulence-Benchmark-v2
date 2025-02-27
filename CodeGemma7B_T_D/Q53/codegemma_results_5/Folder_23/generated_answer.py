def palindrome_of_length_at_least_n(text):
    text = text.lower()
    result = set()
    palindrome_length = 19
    for start in range(len(text)):
        for end in range(start + palindrome_length - 1, len(text)):
            candidate = text[start:end + 1]
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result