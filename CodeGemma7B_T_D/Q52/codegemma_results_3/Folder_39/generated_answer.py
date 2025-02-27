def palindrome_of_length_n(str):
    ans = set()
    str = str.lower()
    for i in range(len(str)):
        for k in range(i + 1, len(str) + 1):
            if str[i:k] == str[i:k][::-1]:
                ans.add(str[i:k])
    return ans