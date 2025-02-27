def palindrome_of_length_n(string):
    string = string.lower()
    return set((string[i:i + 28] for i in range(len(string) - 28) if string[i:i + 28] == string[i:i + 28][::-1] and string[i:i + 28].isalpha()))