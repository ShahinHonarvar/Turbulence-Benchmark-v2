def palindrome_of_length_at_least_n(text):
    text = text.lower()
    possible_palindrome = []
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            if text[i:j + 1] == text[i:j + 1][::-1]:
                possible_palindrome.append(text[i:j + 1])
    return set(possible_palindrome)