def palindrome_of_length_n(n):
    stack = []
    output = set()
    for char in n:
        stack.append(char)
        if len(stack) > 26:
            stack.pop(0)
        if len(stack) >= 26:
            temp = ''.join(stack[:26][::-1]) + ''.join(stack[26:])
            if temp.lower() == temp:
                output.add(temp)
    return output