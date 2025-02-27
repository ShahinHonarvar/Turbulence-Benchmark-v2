def if_contains_anagrams(str_list):

    def count_sort(nums):
        bucket = [0] * 26
        for n in nums:
            bucket[n] += 1
        for i in range(1, 26):
            bucket[i] += bucket[i - 1]
        ans = [''] * len(nums)
        for n in nums[::-1]:
            index = bucket[n] - 1
            bucket[n] -= 1
            ans[index] = n
        return ans

    def generate_anagrams(str):
        used = [''] * 26
        ans = []
        nums = [ord(c) - ord('a') for c in str]
        nums.sort()

        def dfs(pos):
            if pos == len(str):
                temp = char_arr_to_str(used)
                if len(temp) >= 3 and temp not in ans:
                    ans.append(temp)
                return
            for i in range(26):
                if used[i] == '' and nums[pos] == i:
                    used[i] = str[pos]
                    dfs(pos + 1)
                    used[i] = ''
        char_arr_to_str = lambda arr: ''.join(arr)
        dfs(0)
        return ans
    str_list.sort(key=len, reverse=True)
    ans = []
    for str in str_list:
        str = str.lower()
        anagrams = generate_anagrams(str)
        ans.extend(anagrams)
    ans = count_sort(ans)
    for i in range(len(ans) - 1):
        for j in range(i + 1, len(ans)):
            if ans[i] == ans[j]:
                return True
    return len(ans) >= 19