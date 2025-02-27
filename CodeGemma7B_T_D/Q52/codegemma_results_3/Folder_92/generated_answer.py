def palindrome_of_length_n(str_):
    str_ = str_.lower()
    result = set()
    for i in range(len(str_) - 9):
        for j in range(i + 1, len(str_) - 8 + 1):
            substring = str_[i:j + 1]
            if substring == substring[::-1]:
                result.add(substring)
    return result