def all_substring_of_size_n(str1):
    ans = []
    for i in range(len(str1)):
        for j in range(i + 18, len(str1)):
            if len(set(str1[i:j + 1])) == 18:
                if str1[i:j + 1] not in ans:
                    ans.append(str1[i:j + 1])
    return ans