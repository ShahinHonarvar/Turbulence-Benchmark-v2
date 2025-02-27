def palindrome_of_length_at_least_n(text: str) -> set[str]:
    text = text.casefold()
    palindrome_of_length_at_least_n_set = set()
    for i in range(len(text)):
        for j in range(i, len(text)):
            if text[i:j + 1] == text[i:j + 1][::-1] and len(text[i:j + 1]) >= 85:
                palindrome_of_length_at_least_n_set.add(text[i:j + 1])
    return palindrome_of_length_at_least_n_set