def palindrome_of_length_at_least_n(input_str):

    def is_palindrome(x):
        x = x.lower()
        return x == x[::-1]

    def helper(x, y, output):
        for i in range(10 ** (x - y)):
            output.add(str(i) * y + x + str(i) * y)
    x = len(str(10 ** (n // 2)))
    for y in range(x, 90):
        output = set()
        helper(x, y, output)
        if any((is_palindrome(s) for s in output)):
            return output
    return set()