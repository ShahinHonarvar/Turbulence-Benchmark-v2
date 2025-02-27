def palindrome_of_length_n(str):
    temp = str.lower()
    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            window = temp[i:j + 1]
            if len(window) == 77 and window == window[::-1]:
                return window
    return set()