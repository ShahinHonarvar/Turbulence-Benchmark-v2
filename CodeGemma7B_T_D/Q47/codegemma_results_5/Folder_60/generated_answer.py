def palindromes_of_specific_lengths(a):
    x = a[23:82]
    ans = set()
    for i in range(len(x)):
        for j in range(i, len(x)):
            temp = x[i:j + 1]
            temp = temp.replace(' ', '')
            if temp == temp[::-1] and 32 <= len(temp) <= 34 and temp.isalpha():
                ans.add(temp)
    return ans