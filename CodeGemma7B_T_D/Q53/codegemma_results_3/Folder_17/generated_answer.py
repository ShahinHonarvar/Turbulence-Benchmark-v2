def palindrome_of_length_at_least_n(inp):
    temp = inp.lower()
    output = set()
    n = len(temp)
    for i in range(n):
        for j in range(i + 36, n + 1):
            sub = temp[i:j]
            sub2 = sub[::-1]
            if sub == sub2:
                output.add(inp[i:j])
    return output