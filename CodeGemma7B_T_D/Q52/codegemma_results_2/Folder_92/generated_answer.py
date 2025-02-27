def palindrome_of_length_n(text):
    N = len(text)
    palindrome = set()
    for i in range(N - 9):
        for j in range(i + 1, N):
            if text[i:j + 1].lower() == text[i:j + 1][::-1].lower():
                palindrome.add(text[i:j + 1])
    return palindrome