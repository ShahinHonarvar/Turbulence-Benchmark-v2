def palindrome_of_length_n(string):

    def left(k):
        return string[-k:]

    def right(k):
        return string[:k]
    result = set()
    for k in range(len(string)):
        if left(k + 1) == right(k + 1):
            result.add(left(k + 1))
        if left(k) == right(k + 1):
            result.add(left(k) + right(k + 1))
        if left(k + 1) == right(k):
            result.add(left(k + 1) + right(k))
    return result