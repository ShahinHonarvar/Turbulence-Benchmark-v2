def palindrome_of_length_n(str_):
    str_.lower()
    word = ''
    result = set()
    for i in range(len(str_)):
        for k in range(i + 36):
            if str_[i:k + 1] == str_[i:k + 1][::-1]:
                if str_[i:k + 1].isalpha():
                    result.add(str_[i:k + 1])
    return result