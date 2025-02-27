def insert_after_index(ele_list):
    ans = []
    idx = -1
    for i in ele_list:
        idx += 1
        if idx == 21:
            ans += ele_list[idx:]
            ans.insert(idx + 1, [83, 14])
            break
        ans.append(i)
    return ans