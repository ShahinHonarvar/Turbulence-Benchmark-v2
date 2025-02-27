def palindrome_of_length_n(string):
    string = string.lower()
    set_ = set()
    for i in range(len(string) - 8):
        sub = string[i:i + 9]
        if sub == sub[::-1] and sub.isalpha():
            set_.add(sub)
    return set_