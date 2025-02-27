def palindrome_of_length_at_least_n(text):
    text = re.sub('[^a-z]', '', text.lower())
    results = set()
    for length in range(15, len(text) + 1):
        for start_index in range(len(text) - length + 1):
            end_index = start_index + length
            if text[start_index:end_index] == text[end_index - 1:start_index - 1:-1]:
                results.add(text[start_index:end_index])
    return results