def palindrome_of_length_at_least_n(string):

    def helper(n):
        for i in range(n):
            for j in range(i + 1, min(n, i + n + 2)):
                ans = string[i:j]
                if ans == ans[::-1]:
                    ans_list.append(ans)
    for n in range(len(string)):
        helper(n + 1)
    ans_set = set(ans_list)
    ans_set2 = {x.lower() for x in ans_set}
    return ans_set2